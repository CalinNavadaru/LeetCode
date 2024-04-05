#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    string makeGood(string s) {
        stack<char> stack1;
        for (char c: s) {
            if (stack1.empty()) {
                stack1.push(c);
                continue;
            }
            char last = stack1.top();
            if (last - c == 32 || c - last == 32) {
                stack1.pop();
            } else {
                stack1.push(c);
            }
        }
        string result;
        while (!stack1.empty()) {
            result = stack1.top() + result;
            stack1.pop();
        }
        return result;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
