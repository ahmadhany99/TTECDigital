# Vanity Number Converter

This project was built to convert regular phone numbers into creative, meaningful "vanity numbers" — like turning **74663** into **PHONE** — using AWS services.

It’s part of a serverless solution that uses **AWS Lambda**, **DynamoDB**, and (eventually) **Amazon Connect**, where a caller can dial a number and hear vanity suggestions spoken back to them.

---

## ✅ What’s Done So Far

- ✔️ Local script that converts phone numbers to letter combinations
- ✔️ Dictionary-based logic to score and rank the best combinations
- ✔️ Lambda function that handles requests and returns top 5 matches
- ✔️ Stores each request and result in DynamoDB
- ⏳ Amazon Connect phone flow integration (waiting on phone number quota)
- 🧾 Final documentation + cleanup in progress

---

## 📘 In Plain English

When someone calls in or sends a phone number:

1. The script figures out every possible way the number could be spelled using letters on a keypad.
2. It checks which of those combinations include real English words.
3. It scores them based on how many words they include and where those words appear.
4. It returns the best 5 matches and saves everything (input + results) in DynamoDB.

---

## 🔁 Example

**Input phone number:** `74663`  
**Top result might be:** `"SHOOD"`  
**Matched words:** `["SHO"]`

---

## 🗃️ DynamoDB Table

I created a table called `VanityCalls` where each entry includes:

- The original caller’s phone number
- A timestamp
- The top 5 vanity number suggestions (as JSON)

---

## 💻 AWS Lambda

The Lambda function:

- Is written in Python
- Reads from a dictionary file (`20k.txt`)
- Returns results as a JSON object
- Logs everything to DynamoDB
- Will eventually be connected to Amazon Connect so people can call in and hear the results

Handler:

```python
vanity_numbers.lambda_handler
```

## AWS Services Used

- **AWS Lambda**: Converts phone numbers to vanity words
- **DynamoDB**: Stores each caller's number and results
- **Amazon Connect** (in progress): Will read out top 3 suggestions

