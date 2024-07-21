class SupermarketCheckout:
    lines = []
    def on_customer_enter(self, customer_id, line_number, num_items):
        # TODO Implement
        if len(self.lines) < line_number :
            self.lines.append([[customer_id, num_items, num_items]])
        else :
            self.lines[line_number - 1].append([customer_id, num_items, num_items])
        pass

    def on_basket_change(self, customer_id, new_num_items):
        # TODO Implement
        i = 0
        j = 0
        # Find customer first
        while i < len(self.lines) :
            j = 0
            while j < len(self.lines[i]) :
                if self.lines[i][j][0] == customer_id :
                    break
                j += 1
            if j < len(self.lines[i]) and self.lines[i][j][0] == customer_id :
                break
            i += 1
        if i >= len(self.lines) :
            return
        # If new num items more than old, then move them to the end
        if self.lines[i][j][2] < new_num_items :
            initial_items = self.lines[i][j][2]
            self.lines[i].append([customer_id, self.lines[i][j][1] + new_num_items - initial_items, initial_items])
            self.lines[i].pop(j)

        # Set customers items to new num items
        elif new_num_items == 0 :
            self.lines[i].pop(j)
        else :
            self.lines[i][j][1] = new_num_items

    def on_line_service(self, line_number, num_processed_items):
        # TODO Implement
        processed = num_processed_items
        for line in self.lines:
            while processed > 0: 
                # Empty line
                if len(line) == 0:
                    break
                # First customer only has < processed items to check out
                if line[0][1] < processed:
                    processed -= line[0][1]
                    self.on_customer_exit(line[0][0])
                    line.pop(0)
                # First customer has more than or equal to processed items left
                else:
                    line[0][1] -= processed
                    processed = 0
                    if line[0][1] == 0 :
                        self.on_customer_exit(line[0][0])
                        line.pop(0)

    def on_lines_service(self):
        # TODO Implement
        for line in self.lines:
            # Empty line
            if len(line) == 0:
                continue
            # First customer only has 1 item to check out
            if line[0][1] == 1:
                self.on_customer_exit(line[0][0])
                line.pop(0)
            # First customer has more than 1 item
            else:
                line[0][1] -= 1

    def on_customer_exit(self, customer_id):
        # Don't change this implementation.
        print(customer_id)


if __name__ == "__main__":
    import sys

    checkout_tracker = SupermarketCheckout()
    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "CustomerEnter":
            customer_id = int(line[1])
            line_number = int(line[2])
            num_items = int(line[3])
            checkout_tracker.on_customer_enter(customer_id, line_number, num_items)
        elif line[0] == "BasketChange":
            customer_id = int(line[1])
            new_num_items = int(line[2])
            checkout_tracker.on_basket_change(customer_id, new_num_items);
        elif line[0] == "LineService":
            line_number = int(line[1])
            num_processed_items = int(line[2])
            checkout_tracker.on_line_service(line_number, num_processed_items);
        elif line[0] == "LinesService":
            checkout_tracker.on_lines_service();
        else:
            raise Exception("Malformed input!")
