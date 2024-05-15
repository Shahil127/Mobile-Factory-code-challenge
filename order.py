

import uuid
from components import components

class Order:
    def __init__(self, component_codes):
        self.component_codes = component_codes
        self.order_id = str(uuid.uuid4())
        self.total = 0
        self.parts = []

    def is_valid(self):
        if len(set(self.component_codes)) != 5:
            return False
        return all(code in components for code in self.component_codes)

    def calculate_total(self):
        for code in self.component_codes:
            part_info = components[code]
            self.total += part_info['price']
            self.parts.append(part_info['part'])

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'total': round(self.total, 2),
            'parts': self.parts
        }
