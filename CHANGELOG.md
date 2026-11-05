# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-05
### Added
- Sắp xếp đĩa trong giỏ hàng: sort_by_title() và sort_by_cost().
- Tìm kiếm đĩa theo thể loại: search_by_category().

## [1.0.0] - 2026-11-05
### Added
- Cart.print_cart() hiển thị giỏ hàng chi tiết.
- Hàm search_by_title() tìm kiếm đĩa theo tiêu đề.
- Tính năng tính chiết khấu total_cost_with_discount().
- Bộ kiểm thử tự động với unittest (tests/test_cart.py).

### Fixed
- Lỗi giỏ hàng nhận đĩa thứ 21 vượt quá giới hạn 20 đĩa (#6).
- Thông báo thêm đĩa vào giỏ hàng được chuẩn hóa và bản địa hóa.
