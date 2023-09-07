- generate python code from proto file:
```
python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. grpc_def/grpc_route.proto
```
- Run:
```
python -m socketsv.socketsv
```
