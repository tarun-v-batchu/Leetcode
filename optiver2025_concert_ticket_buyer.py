class ConcertTicketBuyer:
    def __init__(self):
        self.tickets = []
        self.artist_id = -1
        self.ticket_price = -1
        self.available_seats = -1
        self.queue = []
        pass
        # Implement constructor if needed

    def on_new_requirement(self, artist_id: int, ticket_price: int, available_seats: int):
        # Write code here
        self.artist_id = artist_id
        self.ticket_price = ticket_price
        self.available_seats = available_seats
        pass

    def process_data(self, message_id: int, data: int):
        # Write code here
        if message_id not in [i[0] for i in self.tickets] :
            self.tickets.append([message_id, data])
        else:
            for i in self.tickets:
                if i[0] == message_id:
                    i.append(data)
                    if len(i) == 4 and i[1] == self.artist_id and i[2] < self.ticket_price and i[3] >= self.available_seats :
                        self.queue.append(i[0])
                        self.queue.append(self.available_seats)
                        top = self.queue.pop(0)
                        return top
        if len(self.queue) == 0 :
            return 0
        else :
            top = self.queue.pop(0)
            return top
                        

if __name__ == "__main__":
    import sys

    read_line = lambda: sys.stdin.readline().split()

    first_line = read_line()
    num_queries = int(first_line[0])

    engine = ConcertTicketBuyer()

    for _ in range(num_queries):
        line = read_line()
        if line[0] == 'REQUIREMENT':
            artist_id = int(line[1])
            ticket_price = int(line[2])
            available_seats = int(line[3])
            engine.on_new_requirement(artist_id, ticket_price, available_seats)
        elif line[0] == "DATA":
            message_id = int(line[1])
            data = int(line[2])
            received = engine.process_data(message_id, data)
            print(received)
        else:
            print("Malformed input!")
            exit(-1)
