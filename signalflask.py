from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# 檢查並創建CSV文件和標題行
csv_file = 'alerts.csv'
csv_columns = ['ticker', 'signal']

if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()

@app.route('/webhook', methods=['POST'])
def webhook():
    # 記錄請求標頭和內容類型
    print('Headers:', request.headers)
    print('Content-Type:', request.content_type)
    print('Data:', request.data)

    # 嘗試解析JSON數據
    try:
        data = request.get_json(force=True)  # 強制解析JSON
        print('Parsed JSON data:', data)
    except Exception as e:
        print('Error parsing JSON:', e)
        data = None

    # 嘗試解析表單數據
    if not data:
        data = request.form.to_dict()
        print('Parsed form data:', data)

    if data:
        # 處理接收到的數據
        handle_alert(data)
        return jsonify({'status': 'success'}), 200
    else:
        print('No data received')
        return jsonify({'status': 'failure', 'reason': 'no data received'}), 400

def handle_alert(data):
    # 根據接收到的數據執行交易策略
    print('Handling alert:', data)
    write_to_csv(data)
    # 在此處添加你的交易策略邏輯

def write_to_csv(data):
    # 將數據寫入CSV文件
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writerow(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # 使用80埠
