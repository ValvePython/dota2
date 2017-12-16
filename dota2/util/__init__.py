
def replay_url(match_id, cluster, replay_salt, app_id=570):
    """Form url for match replay

    :param match_id: match id
    :type  match_id: :class:`int`
    :param cluster: cluster the match is saved on
    :type  cluster: :class:`int`
    :param replay_salt: salt linked to the replay
    :type  replay_salt: :class:`int`
    :param app_id: (optional) app_id for dota
    :type  app_id: :class:`int`
    :return: url to download the replay of a specific match
    :rtype: :class:`str`
    """
    return 'http://replay{0}.valve.net/{1}/{2}_{3}.dem.bz2'.format(cluster, app_id, match_id, replay_salt)


def replay_url_from_match(match, app_id=570):
    """Form url for match replay

    :param match: `CMsgDOTAMatch <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_common.proto#L866-L1001>`_
    :type  match: proto message
    :param app_id: (optional) app_id for dota
    :type  app_id: :class:`int`
    :return: url to download the replay of a specific match, None if match has not all the information
    :rtype: :class:`str`, :class:`None`
    """
    if match.HasField('match_id') and match.HasField('cluster') and match.HasField('replay_salt'):
        return replay_url(match.match_id, match.cluster, match.replay_salt, app_id)


def metadata_url(match_id, cluster, replay_salt, app_id=570):
    """Form url for match metadata file

    :param match_id: match id
    :type  match_id: :class:`int`
    :param cluster: cluster the match is saved on
    :type  cluster: :class:`int`
    :param replay_salt: salt linked to the replay
    :type  replay_salt: :class:`int`
    :param app_id: (optional) app_id for dota
    :type  app_id: :class:`int`
    :return: url to download the metadata of a specific match
    :rtype: :class:`str`
    """
    return 'http://replay{0}.valve.net/{1}/{2}_{3}.meta.bz2'.format(cluster, app_id, match_id, replay_salt)


def metadata_url_from_match(match, app_id=570):
    """Form url for match metadata file

    :param match: `CMsgDOTAMatch <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_common.proto#L866-L1001>`_
    :type  match: proto message
    :param app_id: (optional) app_id for dota
    :type  app_id: :class:`int`
    :return: url to download the metadata of a specific match, None if match has not all the information
    :rtype: :class:`str`, :class:`None`
    """
    if match.HasField('match_id') and match.HasField('cluster') and match.HasField('replay_salt'):
        return metadata_url(match.match_id, match.cluster, match.replay_salt, app_id)
