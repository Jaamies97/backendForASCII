from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/axel_ojut', methods=['GET'])
def convertionfstr():
    sumofascii = 0
    dictionary = {"1": {},
                  "2": {}}
    inputstr = str(request.args['query'])
    for char in inputstr:
        sumofascii += ord(char)
        if char not in dictionary["2"]:
            dictionary["2"][char] = 1
        else:
            dictionary["2"][char] += 1

    dictionary["1"] = str(sumofascii)
    return dictionary


if __name__ == '__main__':
    app.run()