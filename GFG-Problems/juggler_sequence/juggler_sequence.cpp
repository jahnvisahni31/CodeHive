
class Solution {
  public:
    vector<long long> jugglerSequence(long long n) {
        // code here
        std::vector<long long> sequence;
        sequence.push_back(n);

        while (n != 1) {
            if (n % 2 == 0) {
                n = std::sqrt(n);  // Square root rounded down
            } else {
                n = std::sqrt(std::pow(n, 3));  // Cube root rounded down
            }

            sequence.push_back(n);
        }

        return sequence;
    }
};
