from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'weibo')

def set(username, password):
    result = conn.set(username, password)
    if result:
        print('账号', username, '密码', password)
        print('录入成功')
    else:
        #如果插入失败，说明username已存在。删除重新插入
        conn.delete(username)
        set(username,password)

def scan(sep='----'):
    print('正在读取密码本')
    with open('account_pwd.txt') as f:
        accounts = f.readlines()
        for account in accounts:
            username, password = account.split(sep)
            #去掉密码结尾的换行符
            password = password.strip()
            set(username, password)

if __name__ == '__main__':
    scan()