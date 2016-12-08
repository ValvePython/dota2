def format_replay_url(match_id, cluster, replay_salt):
    """Format the url to download a match replay

    :param match_id: match id
    :type match_id: :class: `int`
    :param cluster: cluster the match is saved on
    :type cluster: :class: `int`
    :param replay_salt: salt linked to the replay
    :type replay_salt: :class: `int`
    :return url to download the replay of a specific match
    :rtype :class: `str`
    """
    return 'http://replay{0}.valve.net/570/{1}_{2}.dem.bz2'.format(cluster, match_id, replay_salt)

def format_replay_url_from_match(match):
    """Format the url to download a match replay

    :param match: `CMsgDOTAMatch <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_common.proto#L866-L1001>`_
    :type  match: proto message
    :return url to download the replay of a specific match, None if match has not all the information
    :rtype :class: `str`
    """
    if match.match_id and match.cluster and match.replay_salt:
        return Match.format_replay_url(match.match_id, match.cluster, match.replay_salt)
    else:
        return None

def format_metadata_url(match_id, cluster, replay_salt):
    """Format the url to download a match metadata

    :param match_id: match id
    :type match_id: :class: `int`
    :param cluster: cluster the match is saved on
    :type cluster: :class: `int`
    :param replay_salt: salt linked to the replay
    :type replay_salt: :class: `int`
    :return url to download the metadata of a specific match
    :rtype :class: `str`
    """
    return 'http://replay{0}.valve.net/570/{1}_{2}.meta.bz2'.format(cluster, match_id, replay_salt)

def format_metadata_url_from_match(match):
    """Format the url to download a match metadata

    :param match: `CMsgDOTAMatch <https://github.com/ValvePython/dota2/blob/e06c81c03579a912fcca829766ee590075ae97dc/protobufs/dota_gcmessages_common.proto#L866-L1001>`_
    :type  match: proto message
    :return url to download the metadata of a specific match, None if match has not all the information
    :rtype :class: `str`
    """
    if match.match_id and match.cluster and match.replay_salt:
        return Match.format_metadata_url(match.match_id, match.cluster, match.replay_salt)
    else:
        return None
