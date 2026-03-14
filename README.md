# 📖 Workflow GitHub Actions CI/CD
Nội dung file giải thích cấu trúc và cách hoạt động của file cấu hình .github/workflows/main.yml

## 1. Khi nào Pipeline này hoạt động? (Trình kích hoạt - Events)
Hệ thống được cấu hình để tự động kích hoạt con robot (Runner) của GitHub chạy trong 2 trường hợp:
- **push**: Khi có bất kỳ code được đẩy (push) mới trực tiếp lên nhánh main.
- **pull_request**: Khi có một yêu cầu kéo (pull request) được tạo hoặc cập nhật hướng đến nhánh main. Hệ thống sẽ chạy test trước để kiểm duyệt xem code có an toàn để gộp hay không.

## 2. Các luồng công việc (Jobs)
### 🛠️ Job 1: ci-test-job (Kịch bản 1 - CI Pipeline Cơ Bản)
- **Môi trường chạy**: ubuntu-latest
- **Nhiệm vụ**: Chạy các bài kiểm thử tự động để đảm bảo mã nguồn không có lỗi.
- **Trạng thái hiện tại**: Đang để Dummy (giả lập).

### 📦 Job 2: cd-build-artifact (Kịch bản 2 - CD Pipeline Cơ Bản)
- **Điều kiện thực thi 1 (needs: ci-test-job)**: Job này bắt buộc phải đợi ci-test-job chạy thành công 100% thì mới được bắt đầu. Nếu test rớt, quy trình dừng lại ngay lập tức.

- **Điều kiện thực thi 2 (if)**: Chỉ thực hiện đóng gói khi có hành động push vào thẳng nhánh main. (Nếu chỉ là tạo Pull Request thì không cần nén file tốn tài nguyên).

- Các bước thực hiện:
1. **Lấy mã nguồn**: Sử dụng actions/checkout@v4 để kéo code về.
2. **Nén thư mục**: Dùng lệnh zip để nén toàn bộ thư mục src/ thành file calculator.zip.
3. **Tải lên Artifact**: Dùng actions/upload-artifact@v4 để đẩy file zip lên giao diện GitHub, cho phép người dùng click tải về.


## 📌 Ghi chú quan trọng (Về Kịch bản 2 - CD)
Hiện tại, file `.github/workflows/main.yml` đang được tinh chỉnh tạm thời để phục vụ việc **kiểm thử độc lập Kịch bản 2 (CD Build Artifact)**

### 🛠️ Những thay đổi tạm thời trong `main.yml`
Đã **comment lại** một số điều kiện ràng buộc. Cụ thể:
1. `needs: ci-test-job` (ở Job 2): Tạm tắt để Job đóng gói chạy tự do, không cần chờ Job 1 hoàn thành.
2. `if: github.event_name == 'push' && github.ref == 'refs/heads/main'` (ở Job 2): Tạm tắt để có thể test kịch bản trên các nhánh phụ.
3. Phần `on: push`: Tạm đổi thành `branches: [ '**' ]` để có thể trigger workflow trên mọi nhánh.

## Merge Code 
**Khi ghép code, CẦN PHỤC HỒI các dòng sau trong `main.yml` (xóa dấu `#`):**
- [ ] Mở lại `needs: ci-test-job` để đảm bảo code test pass mới được build.
- [ ] Mở lại `if: ...` để chỉ cho phép build Artifact khi push code lên nhánh `main`.
- [ ] Đổi lại cấu hình trigger thành `branches: [ main ]`.


