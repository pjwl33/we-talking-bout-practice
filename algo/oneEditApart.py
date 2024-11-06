#
# Question 3: Edit Distance
# Write a function that returns whether two words are exactly "one edit" away using the following signature:
# bool OneEditApart(string s1, string s2);
# An edit is:
# Inserting one character anywhere in the word (including at the beginning and end)
# Removing one character
# Replacing one character

# Solution
# There are many solutions to this problem. One optimal solution is to walk each string in unison, tracking if a difference has been encountered. If a second difference is encountered, return false. If one string is longer than the other, then the difference must mean it is an insertion, so skip a character in the longer string and continue. Additionally, there are symmetry and short circuit opportunities.
# Sample Solution in C++
# bool one_edit_apart(const string* s1, const string* s2) {
#   if (s1->size() > s2->size())
#     swap(s1, s2);
#   if (s2->size() - s1->size() > 1)
#     return false;
#   bool saw_difference = false;
#   for (size_t i = 0, j = 0; i < s1->size(); ++i, ++j) {
#     if ((*s1)[i] != (*s2)[j]) {
#       if (saw_difference) return false;
#       saw_difference = true;
#       if (s2->size() > s1->size()) {
#         --i;
#       }
#     }
#   }
#   return saw_difference || s2->size() != s1->size();
# }

def oneEditApart(s1, s2): # -> bool
    # ensure that s1 is the shorter string
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # if size difference is more than one, not possible to be 1 apart
    if len(s2) - len(s1) > 1:
        return False

    diff = False
    i, j = 0, 0 # pointers for s1 and s2

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if diff:
                return False

            diff = True
            # If strs are diff in length, skip char in longer string
            if len(s2) > len(s1):
                i -= 1

        i += 1
        j += 1

    return diff or len(s1) != len(s2)

# Examples:
print(oneEditApart("cat", "dog"), "false")
print(oneEditApart("cat", "cats"), "true")
print(oneEditApart("cat", "cut"), "true")
print(oneEditApart("cat", "cast"), "true")
print(oneEditApart("cat", "at"), "true")
print(oneEditApart("cat", "act"), "false")
