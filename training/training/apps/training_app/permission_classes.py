from rest_framework import permissions

from . import models


def get_ip(req):
    ip = req.META['REMOTE_ADDR']
    # forwarded proxy fix for proxy passing setups
    if (not ip or ip == '127.0.0.1') and req.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = req.META['HTTP_X_FORWARDED_FOR']
    return ip


def is_ip_in_nets(ip, nets):
    for net in nets:
        if ip in net:
            return True
    return False


class WhiteListorAPIPermission(permissions.BasePermission):
    """
        Global permission check for white listed IPs.
    """
    def has_permission(self, request, view):
        request_ip = get_ip(request)
        trusted_ips = [i.get_network() for i in models.TrustedIP.objects.only('network')]
        return is_ip_in_nets(request_ip, trusted_ips)