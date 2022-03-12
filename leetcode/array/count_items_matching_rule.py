class Solution:
    def count_matches(self, items: list, rule_key: str, rule_value: str) -> int:
        hashtable = {"type": [], "color": [], "name": []}
        for item in items:
            hashtable["type"].append(item[0])
            hashtable["color"].append(item[1])
            hashtable["name"].append(item[2])
        count = 0
        for value in hashtable[rule_key]:
            if value == rule_value:
                count += 1
        return count

    def count_matches_easy(self, items: list, rule_key: str, rule_value: str) -> int:
        search_index = 0
        if rule_key == "color":
            search_index = 1
        elif rule_key == "name":
            search_index = 2
        count = 0
        for item in items:
            if item[search_index] == rule_value:
                count += 1
        return count


items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
solution = Solution()
print(solution.count_matches_easy(items, ruleKey, ruleValue))
