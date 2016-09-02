import ldap
import ldap.modlist as modlist
import ldif
import sys


ldif_writer = ldif.LDIFWriter(sys.stdout)

from ldap.controls import SimplePagedResultsControl

ldap.set_option(ldap.OPT_REFERRALS, 0)
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)


def create_domain_user(lcon_emg, first_name, las_name, password, email, agent_type, country_name, state_name,
                       department, address, zipcode, title):
    # SCRIPT = 1
    # ACCOUNTDISABLE = 2
    # HOMEDIR_REQUIRED = 8
    # PASSWD_NOTREQD = 32
    # NORMAL_ACCOUNT = 512
    # DONT_EXPIRE_PASSWORD = 65536
    # TRUSTED_FOR_DELEGATION = 524288
    # PASSWORD_EXPIRED = 8388608
    # ad_u['userAccountControl'] = str(NORMAL_ACCOUNT + ACCOUNTDISABLE)

    username = email.split('@')[0]
    ad_u = {}
    ad_u['objectClass'] = ['top', 'person', 'organizationalPerson', 'user']
    ad_u['cn'] = '{} {}'.format(first_name, las_name)
    ad_u['userPassword'] = password
    ad_u['mail'] = email
    ad_u['givenName'] = first_name
    ad_u['sn'] = las_name
    ad_u['description'] = agent_type
    ad_u['objectCategory'] = "CN=Person,CN=Schema,CN=Configuration,DC=corp,DC=hbcinsure,DC=com"
    ad_u['co'] = country_name,
    ad_u['department'] = department
    ad_u['displayName'] = '{} {}'.format(first_name, las_name)
    ad_u['l'] = address
    ad_u['postalCode'] = zipcode
    ad_u['sAMAccountName'] = username
    ad_u['st'] = state_name
    ad_u['title'] = title
    ad_u['userPrincipalName'] = email

    distinguishedName = "CN={},OU=Regular users,OU=USA,OU=Health Benefit Center,DC=corp,DC=hbcinsure,DC=com".format(
        username)
    mods = modlist.addModlist(ad_u)
    result = {}
    try:
        lcon_emg.add_s(distinguishedName, mods)
    except Exception, e:
        lcon_emg.unbind_s()
        result = {'error_ad': 'ActiveD: Error  %s' % str(e)}
    else:
        result = {'success_ad': 'ActiveD: F4ck y34h'}

    if result.get('success_ad'):
        # then you can put a password for the user is a default enabled account
        unicode_pass = unicode('\"{} \"'.format(password), 'iso-8859-1')
        password_value = unicode_pass.encode('utf-16-le')
        add_pass = [(ldap.MOD_REPLACE, 'unicodePwd', [password_value])]
        # 512 will set user account to enabled
        mod_acct = [(ldap.MOD_REPLACE, 'userAccountControl', '514')]

        try:
            lcon_emg.modify_s(ad_u.get('distinguishedName'), add_pass)
        except ldap.LDAPError, error_message:
            lcon_emg.unbind_s()
            result = {'error_ad_clave': 'ActiveD: Error %s' % str(error_message)}
            return result
        else:
            result = {'success_ad_clave': 'ActiveD: Yeah'}

        try:
            lcon_emg.modify_s(ad_u.get('distinguishedName'), mod_acct)
        except ldap.LDAPError, error_message:
            lcon_emg.unbind_s()
            result = {'error_ad_hab': 'Error  %s' % str(error_message)}
            return result
        else:
            lcon_emg.unbind_s()
            result = {'success_ad_hab': 'Success'}
    return result


def authenticate(domain_value, username, password):
    conn = ldap.initialize('ldap://' + domain_value)
    conn.protocol_version = 3
    error_msj = ''
    try:
        result = conn.simple_bind_s(username, password)
    except ldap.INVALID_CREDENTIALS:
        error_msj = "Invalid credentials"
    except ldap.SERVER_DOWN:
        error_msj = "Server down"
    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            error_msj = "Other LDAP error: " + e.message['desc']
        else:
            error_msj = "Other LDAP error: " + e
    except Exception, e:
        error_msj = e.message
    return error_msj, conn


def search_domain_user(conn, domain_value, search_string):
    domain_split = domain_value.split('.')
    basedn = ",".join('dc={}'.format(dc) for dc in domain_split)
    value_result = []
    error_msj = ''
    if '@' in search_string:
        user_filter = '(mail=*{}*)'.format(search_string)
    else:
        user_filter = '(sAMAccountName={})'.format(search_string)
    # user_filter = '(&(objectClass=person)(sAMAccountName=dak))'

    try:
        result_id = conn.search_s(basedn, ldap.SCOPE_SUBTREE, user_filter)
        for dn,entry in result_id:
            a = ldif_writer.unparse(dn,entry)
            print a

        # for item in result_id:
        #     l = list(item)
        #     for entry in l:
        #         if 'cn' in str(entry):
        #             mail = entry.get('mail')
        #             if mail:
        #                 mail = mail[0]
        #                 print 'email:{}'.format(mail), ' - ', 'fullname:{}'.format(entry['cn'][0])
        #                 value_result.append({'email': mail, 'fullname': entry['cn'][0]})

    except ldap.LDAPError, e:
        error_msj = e.message
    conn.unbind_s()

    return value_result, error_msj


def main():
    error_msj, conn = authenticate(domain_value='hbcoakdc1.corp.hbcinsure.com', username='CORP\svc_unicorn', password='HBC@dmin42015$')
    domain_users, error_msj = search_domain_user(conn, domain_value='corp.hbcinsure.com', search_string='YTest')
#     if not msj:
#         create_domain_user(conn, 'TestFirst', 'TestLast', 'TestY123456', 'TestFirst@simplehealthplans.com')
#     print msj
#
#     # search_domain_user('ypineiro')
#
#
if __name__ == '__main__':
    main()
