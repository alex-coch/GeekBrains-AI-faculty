

def get_user_agent(plugin=None):
    ver = sys.version_info
    python_version = '%d.%d.%d.%s.%d' % (ver[0], ver[1], ver[2], ver[3], ver[4])
    user_agent = u('wakatime/{ver} ({platform}) Python{py_ver}').format(
        ver=u(__version__),
        platform=u(platform.platform()),
        py_ver=python_version,
    )
    if plugin:
        user_agent = u('{user_agent} {plugin}').format(
            user_agent=user_agent,
            plugin=u(plugin),
        )
    else:
        user_agent = u('{user_agent} Unknown/0').format(
            user_agent=user_agent,
        )
    return user_agent

print(get_user_agent)