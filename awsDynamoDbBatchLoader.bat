@echo off
for %%f in (ZDB*%1_TaperShow.json) do (
    echo %%~nf.json
    aws dynamodb batch-write-item --request-items file://%%~nf.json
)
