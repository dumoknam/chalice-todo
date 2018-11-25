# setup

## make s3 bukcet

```bash
aws s3 mb s3://chalice-올릴-버켓-이름/ --region ap-northeast-2
```

# deploy

## 1. make package

```bash
chalice package packaged/
```

## 2. cloudformation package

```bash
aws cloudformation package --template-file ./sam.json \
    --s3-bucket chalice-올릴-버켓-이름 \
    --output-template-file sam-packaged.yaml
```

## 3. cloudformation deploy

```bash
aws cloudformation deploy --template-file ./sam-packaged.yaml \
    --stack-name chalice-올릴-스택명 \
    --capabilities CAPABILITY_IAM
```

## 4. verification

```bash
aws cloudformation describe-stacks --stack-name chalice-올릴-스택명 \
    --query 'Stacks[0].StackStatus'
```

# delete

## 1. stack

```
aws cloudformation delete-stack --stack-name chalice-올릴-스택명
```

## 2. wait for deletion

```
aws cloudformation wait stack-delete-complete \
    --stack-name chalice-올릴-스택명
```

## 3. s3 bucket

```
aws s3 rb --force s3://chalice-올릴-버켓-이름/ \
    --region ap-northeast-2
```
