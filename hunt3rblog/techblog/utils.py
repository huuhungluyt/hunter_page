from .models import Topic, Log


def get_client_ip(request):
    x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def context_processor(request):
    log_access(request)
    topics=Topic.objects.order_by('-time_created')
    return {'topics':topics}


def log_access(request):
    ip_addr= get_client_ip(request)
    url= request.build_absolute_uri('?')
    log=Log(ip_addr=ip_addr, action='hit', accessed_url=url)
    log.save()

def log_comment(request, user, comment):
    ip_addr= get_client_ip(request)
    url= request.build_absolute_uri('?')
    log=Log(ip_addr=ip_addr, user=user, message=comment, action='cmt', accessed_url=url)
    log.save()