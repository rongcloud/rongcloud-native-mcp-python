from shlex import quote

def request_to_curl(request, compressed=False, verify=True):
    """ request 请求转成 curl 连接
    @param request:
    @param compressed:
    @param verify: 是否需要强制认证
    @return:
    """
    parts = [
        ('curl', None),
        ('-X', request.method),
    ]

    for k, v in sorted(request.headers.items()):
        if 'Accept-Encoding' in k:
            continue
        if 'Content-Length' in k:
            continue
        parts += [('-H', '{0}: {1}'.format(k, v))]

    if request.body:
        body = request.body
        if isinstance(body, bytes):
            body = body.decode('utf-8')
        parts += [('-d', body)]

    if compressed:
        parts += [('--compressed', None)]

    if not verify:
        parts += [('--insecure', None)]

    parts += [(None, request.url)]

    flat_parts = []
    for k, v in parts:
        if k:
            flat_parts.append(quote(k))
        if v:
            flat_parts.append(quote(v))

    return ' '.join(flat_parts)
