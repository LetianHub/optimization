#include <cstdlib>
#include <ctime>
#include <iostream>
#include <queue>

using namespace std;

struct Node {
  int data;
  Node* left;
  Node* right;

  Node(int data) {
    this->data = data;
    left = right = nullptr;
  }
};

Node* generateFixedTree(int height, int minVal, int maxVal) {
  if (height == 0) {
    return nullptr;
  }

  Node* root = new Node(rand() % (maxVal - minVal + 1) + minVal);
  root->left = generateFixedTree(height - 1, minVal, maxVal);
  root->right = generateFixedTree(height - 1, minVal, maxVal);

  return root;
}

void deleteTree(Node* root) {
  if (root == nullptr) {
    return;
  }

  deleteTree(root->left);
  deleteTree(root->right);
  delete root;
}

void printBT(const std::string& prefix, const Node* node, bool isLeft) {
  if (node != nullptr) {
    std::cout << prefix;

    std::cout << (isLeft ? "├──" : "└──");

    // print the value of the node
    std::cout << node->data << std::endl;

    // enter the next tree level - left and right branch
    printBT(prefix + (isLeft ? "│   " : "    "), node->left, true);
    printBT(prefix + (isLeft ? "│   " : "    "), node->right, false);
  }
}

void printBT(const Node* node) { printBT("", node, false); }

int main() {
  srand(time(NULL));

  int height = 5;  // 4 layers
  int minVal = 1;
  int maxVal = 10;

  Node* root = generateFixedTree(height, minVal, maxVal);

  cout << "Fixed Binary Tree:" << endl;
  printBT(root);

  deleteTree(root);

  return 0;
}