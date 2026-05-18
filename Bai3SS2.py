# Phân tích 
#Đầu vào chúng ta cần 2 biến là họ và tên và tuổi, sau đó chúng ta check tên và tuổi với câu lệnh điều kiện 
#Với cách check thì tên nếu trống thì in ra tên không hợp lệ còn nếu tổi âm hoặc lớn hơn 200 thì in ra là tuổi nằm ngoài phạm vi con người 
#Sau đó dùng câu lệnh điều kiện cho tuổi hợp lệ để phù hợp với đề bài đưa ra  

name_patient = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn")) 

if name_patient == "":
    print("Tên không hợp lệ")
elif age < 0  or  age > 200:
    print("Tuổi không hợp lệ")
elif age < 6: 
    print("ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi")
elif age > 80:
    print("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa")
else: 
    print("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh")