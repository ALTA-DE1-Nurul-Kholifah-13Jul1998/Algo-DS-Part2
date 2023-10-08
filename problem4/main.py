def count_item_and_sort(items):
    count = {}

    for i in sorted(items):
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    sort_count = sorted(count.items(), key=lambda x: x[1])
    result = " ".join([f"{item}->{count}" for item, count in sort_count])
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"