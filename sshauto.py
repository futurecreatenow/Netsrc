# paramikoのインポート
import paramiko

# 認証情報
IP_ADDRESS = '192.168.56.101'
USER_NAME = 'takayuki'
PASSWORD = 'Suika628'
## パスワードでなくキーファイルの場合は以下
# KEY_FILENAME = '/Users/test/.ssh/aws.pem'

# サーバー上で実行するコマンド
cmd = 'ls' 

# sshクライアントの作成
client = paramiko.SSHClient()
# サーバーのホストキーが見つからなかった場合の設定　自動で追加したい場合はparamiko.AutoAddPolicy()に変更
client.set_missing_host_key_policy(paramiko.WarningPolicy())
# 上記で設定したIPアドレス、ユーザー名、キーファイルを渡す
client.connect(IP_ADDRESS,
               username=USER_NAME,
               password=PASSWORD,
               #key_filename=KEY_FILENAME,
               timeout=3.9)

# コマンドの実行
stdin, stdout, stderr = client.exec_command(cmd)
# コマンド実行結果を変数に格納
cmd_result = ''
for line in stdout:
    cmd_result += line

# 実行結果を出力
print(cmd_result)

# ssh接続断
client.close()
# お作法
del client, stdin, stdout, stderr