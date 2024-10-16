from datetime import timedelta

class Config:
    SECRET_KEY = 'b5d4f2c7e1e2c6d93c8b7d5b9e3f71a2c6d4b5e8f7d6a3b8e4e1b5d4a7f8c6d9a'  # Chìa khóa bí mật
    # Đặt URI kết nối cơ sở dữ liệu PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://hieu:z5SlbmLaNc7AwaNWvxpPxhX6YGZBGvCB@dpg-cs7p2h5umphs73ab1pjg-a:5432/hieu'  # Thay <your_correct_password> bằng mật khẩu đúng
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Tắt theo dõi sửa đổi
    PERMANENT_SESSION_LIFETIME = timedelta(days=5)  # Thời gian sống của phiên là 5 ngày



# from datetime import timedelta


# class Config:
#     SECRET_KEY = 'b5d4f2c7e1e2c6d93c8b7d5b9e3f71a2c6d4b5e8f7d6a3b8e4e1b5d4a7f8c6d9a'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     PERMANENT_SESSION_LIFETIME = timedelta(days=5)
