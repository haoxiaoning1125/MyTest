def get_rank_list_data(rank_list):
    ret = []
    user_data_dic = dict()
    ids = [x[0] for x in rank_list]
    users = session.query(
        BingoUser.id, BingoUser.name, BingoUser.frame_id, BingoUser.facebook_id,
    ).filter(BingoUser.id.in_(ids)).all()

    for user in users:
        user_data_dic[user[0]] = user

    for uid, score in rank_list:
        user_dic = dict(uid=int(uid), score=int(score))
        user_data = user_data_dic.get(uid)
        if user_data:
            user_dic['name'] = user_data[1]
            user_dic['frame'] = user_data[2]
            user_dic['fb'] = user_data[3]
        ret.append(user_dic)
    return ret


if __name__ == '__main__':
    print 3709716 in [1968334, 2500139, 2996948, 3142079, 3207396, 3309692, 4926188, 5721490, 5783565, 6226880, 6339630, 6361461, 7016633, 8240500, 8299887, 8507145, 8865457, 8964915, 10248047, 10374943, 10532055, 10971918, 10990100, 11288380, 11485774, 11575400, 11649428, 13285424, 13809889, 13844611, 14632728, 15989326, 16435697, 16936958, 17401216, 17410575, 18030904, 18398933, 19120517, 19375016, 19791553, 20330951, 20570024, 20883027, 20921537, 21130384, 21497468, 21693034, 21760072, 21848890, 22117303, 22582405, 22685698, 23020231, 23115191, 23368025, 23707447, 23774753, 24030709, 24125675, 24209696, 24218647, 24233335]

