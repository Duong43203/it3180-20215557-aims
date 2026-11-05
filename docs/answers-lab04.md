# Báo cáo thảo luận - Lab 04

## 1. Vì sao `release/*` không merge vào master? So sánh với GitFlow.
- Trong Release Flow (Microsoft / học phần), `master` là nhánh phát triển chính luôn đi về phía trước. Nhánh `release/*` được tạo ra để đóng băng baseline phục vụ việc triển khai, bàn giao hoặc nộp bài. Nếu có sửa lỗi khẩn cấp (hotfix), ta sẽ cherry-pick bản vá đó sang các nhánh cần thiết thay vì merge toàn bộ ngược lại, tránh đưa các thay đổi chưa được kiểm duyệt vào `master`.
- **So sánh với GitFlow**: GitFlow duy trì hai nhánh vĩnh cửu là `master` (production) và `develop` (phát triển). Nhánh release trong GitFlow được tạo từ `develop` và khi phát hành phải merge vào cả `master` lẫn `develop`. Điều này làm luồng phân nhánh phức tạp hơn nhiều so với Release Flow.

## 2. Vì sao đánh số 1.0.0 mà không phải 0.4.0?
- Theo nguyên tắc Semantic Versioning (SemVer), các phiên bản `0.y.z` là giai đoạn phát triển ban đầu, API chưa ổn định.
- Phiên bản `1.0.0` đánh dấu mốc phần mềm hoàn thiện phiên bản đầu tiên sẵn sàng bàn giao cho người dùng (production release/baseline nộp bài chính thức), có đầy đủ tài liệu, kiểm thử và cam kết tính ổn định của API.
