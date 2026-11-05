# Báo cáo thảo luận - Lab 01

## 1. Vì sao dùng `git mv`?
- Lệnh `git mv` thực hiện đồng thời hai thao tác: di chuyển/đổi tên file trên cây thư mục cục bộ và tự động đưa thao tác đó vào Staging Area (`git add`).
- Giúp Git theo dõi được dấu vết đổi tên (rename tracking), bảo toàn toàn bộ lịch sử commit trước đó của tệp khi dùng lệnh kiểm tra `git log --follow -- aims/cart.py`.

## 2. `release/lab01` có phải baseline?
- Có. Nhánh `release/lab01` đóng vai trò là một baseline (mốc cấu hình chuẩn đã được kiểm thử, đóng băng và nghiệm thu) để nộp bài đánh giá Lab 01.

## 3. Vì sao không commit thẳng master dù làm một mình?
- Giữ cho nhánh `master` luôn luôn ở trạng thái "sạch", ổn định và có thể release bất kỳ thời điểm nào.
- Tuân thủ quy trình quản lý cấu hình chuẩn (SCM Flow): mọi thay đổi phải xuất phát từ một nhánh riêng (`refactor/*`, `feature/*`, `bugfix/*`), qua bước kiểm thử độc lập và Pull Request review trước khi tích hợp vào `master`.
