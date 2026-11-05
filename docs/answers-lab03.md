# Báo cáo thảo luận - Lab 03

## 1. Merge base là gì?
- **Merge base** là commit tổ tiên chung gần nhất (best common ancestor) của hai nhánh chuẩn bị merge với nhau.
- Git sử dụng commit merge base trong thuật toán 3-way merge để so sánh sự thay đổi ở cả hai nhánh độc lập nhằm tự động tích hợp mã nguồn hoặc đánh dấu vị trí phát sinh xung đột (conflict).

## 2. Vì sao `master` và `release/*` phải dùng revert thay vì reset?
- `master` và `release/*` là các nhánh chung đã được chia sẻ (public shared branches) với các thành viên khác hoặc môi trường production.
- Lệnh `git reset` dời con trỏ nhánh và xóa bỏ lịch sử commit, dẫn đến sai lệch lịch sử khi push và buộc phải dùng `--force`, gây hỏng repository của đồng đội.
- Ngược lại, `git revert` tạo ra một commit mới để đảo ngược sự thay đổi mà vẫn giữ nguyên tính toàn vẹn của chuỗi lịch sử commit.
