# Self-debank

[English](#english) | [Tiếng Việt](#tiếng-việt)

## English

This project helps you check ETH balances across multiple chains for a list of wallet addresses.

### Getting Started

Follow these steps to set up and run the project:

#### Prerequisites

- Git
- Python 3.6 or higher

#### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Parksybil/Self-debank.git
   cd Self-debank
   ```

2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

#### Usage

1. Create a `wallet.txt` file in the project root directory if it doesn't exist already.

2. Add the wallet addresses you want to check, one per line, to the `wallet.txt` file. For example:
   ```
   0x742d35Cc6634C0532925a3b844Bc454e4438f44e
   0x742d35Cc6634C0532925a3b844Bc454e4438f44f
   ```

3. Run the main script:
   ```
   python main.py
   ```

4. Check the console output for the total ETH balance across all chains and wallets.

5. The script will generate an `allbalance.csv` file with detailed balance information for each wallet on each chain.

### Supported Chains

The script currently supports the following chains:
- Arbitrum
- Base
- zkSync
- Ethereum

You can add more chains by modifying the `chains` dictionary in the script.

### Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.

---

## Tiếng Việt

Dự án này giúp bạn kiểm tra số dư ETH trên nhiều chuỗi blockchain cho một danh sách các địa chỉ ví.

### Bắt đầu

Làm theo các bước sau để cài đặt và chạy dự án:

#### Yêu cầu tiên quyết

- Git
- Python 3.6 trở lên

#### Cài đặt

1. Clone kho lưu trữ:
   ```
   git clone https://github.com/Parksybil/Self-debank.git
   cd Self-debank
   ```

2. Cài đặt các thư viện cần thiết:
   ```
   pip install -r requirements.txt
   ```

#### Sử dụng

1. Tạo một tệp `wallet.txt` trong thư mục gốc của dự án nếu nó chưa tồn tại.

2. Thêm các địa chỉ ví bạn muốn kiểm tra vào tệp `wallet.txt`, mỗi địa chỉ trên một dòng. Ví dụ:
   ```
   0x742d35Cc6634C0532925a3b844Bc454e4438f44e
   0x742d35Cc6634C0532925a3b844Bc454e4438f44f
   ```

3. Chạy script chính:
   ```
   python main.py
   ```

4. Kiểm tra kết quả đầu ra trên console để xem tổng số dư ETH trên tất cả các chuỗi và ví.

5. Script sẽ tạo ra một tệp `allbalance.csv` với thông tin chi tiết về số dư cho mỗi ví trên mỗi chuỗi.

### Các chuỗi được hỗ trợ

Script hiện hỗ trợ các chuỗi sau:
- Arbitrum
- Base
- zkSync
- Ethereum

Bạn có thể thêm nhiều chuỗi khác bằng cách sửa đổi từ điển `chains` trong script.

### Hỗ trợ

Nếu bạn gặp bất kỳ vấn đề hoặc có câu hỏi, vui lòng mở một issue trong kho lưu trữ GitHub.
