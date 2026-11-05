# Báo cáo thảo luận - Lab 02

## 1. Vì sao phải đồng bộ master trước khi gửi PR?
- Giúp nhánh tính năng tích hợp sớm các commit mới nhất từ `master`, phát hiện và giải quyết xung đột (conflict) ngay trên môi trường cục bộ của lập trình viên thay vì làm gãy build trên CI/CD hay gây khó khăn khi merge trên GitHub.
- Đảm bảo kiểm thử tích hợp (integration testing) pass trước khi yêu cầu review.

## 2. Khi nào không được rebase?
- Theo "Quy tắc vàng của Rebase": **Không bao giờ rebase trên các nhánh công khai/chia sẻ (public shared branches)** như `master` hoặc `release/*`. Rebase sẽ viết lại lịch sử (tạo commit hash SHA mới), làm phân kỳ lịch sử của các thành viên khác trong nhóm và dẫn đến xung đột nghiêm trọng.

## 3. `feature/*` khác `topic/*` ra sao?
- Nhánh `feature/*`: Dùng để phát triển một chức năng/tính năng người dùng mới của phần mềm (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- Nhánh `topic/*`: Nhánh chuyên đề ngắn hạn, thường dành cho tài liệu, cấu hình dự án, công việc hạ tầng hoặc thử nghiệm nhỏ (ví dụ: `topic/pr-template`, `topic/use-case-diagram`).
