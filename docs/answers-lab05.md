# Báo cáo thảo luận - Lab 05

## 1. Ưu, nhược điểm của upstream first so với release first?
- **Upstream first (sửa trên `master` trước rồi cherry-pick sang `release/*`)**:
  - *Ưu điểm*: Tránh hoàn toàn nguy cơ bị quên (regression) khi phát triển các phiên bản tương lai; đảm bảo mã nguồn mới nhất luôn có bản sửa lỗi.
  - *Nhược điểm*: Khi cần ra bản vá khẩn cấp cho production, quy trình upstream first có thể mất nhiều thời gian kiểm thử trên `master` (nơi có thể đang có các tính năng dở dang).
- **Release first (sửa trên `release/*` trước rồi cherry-pick về `master`)**:
  - *Ưu điểm*: Tối ưu thời gian xử lý sự cố nóng (hotfix) trên môi trường release/production; cô lập phạm vi sửa lỗi chỉ trên phiên bản bị ảnh hưởng.
  - *Nhược điểm*: Dễ bị sót việc lan truyền bản vá về các nhánh release khác hoặc nhánh `master` nếu không có quy trình kiểm toán (audit) nghiêm ngặt.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- Lệnh: `git cherry -v origin/master origin/release/lab05` hoặc `git log --all --grep "cherry picked from commit <FIX_SHA>"`.
- Lệnh vòng lặp kiểm tra hành vi (behavior test) trên cả 3 ref:
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
    git switch --detach -q $ref; printf "%-8s " $ref
    python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print(len(search_by_title([D('The Lion King')], 'lion')))"
  done; git switch -q master
  ```
  Nếu quên lan truyền sang `release/lab05`, tại `v1.1.0` sẽ in ra `0` thay vì `1`.
