"""
FastAPI的Hello World示例
"""
from fastapi import FastAPI
import uvicorn

# 创建FastAPI应用
app = FastAPI(title="Hello World API")

@app.get("/")
async def root():
    """根路径，返回一个简单的问候"""
    return {"message": "你好，世界!"}

@app.get("/hello/{name}")
async def hello(name: str):
    """带参数的问候"""
    return {"message": f"你好，{name}!"}

if __name__ == "__main__":
    print("启动服务: http://127.0.0.1:8000")
    print("访问示例:")
    print("- http://127.0.0.1:8000/")
    print("- http://127.0.0.1:8000/hello/世界")
    uvicorn.run(app, host="127.0.0.1", port=8000) 