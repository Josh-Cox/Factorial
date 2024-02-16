from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods=["GET"])
def factorial(n):
	r = calculate(n)
	return {"result":r}, 200

def calculate(n):
	result = 1
	for i in range(n):
		result *= i
	return result

if __name__ == "__main__":
	app.run(host="localhost", port=3000)
