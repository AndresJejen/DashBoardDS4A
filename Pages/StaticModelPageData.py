# Numeric Fields
fields = [
            {"Label": "Price", "Description": "Price of device att moment of purchase", "type": "number"},
            {"Label": "Past purchases", "Description": "Number of purchases done by user", "type": "number"},
            {"Label": "Hours elapsed", "Description": "Total hours in local session before pass to checkout", "type": "number"},
            {"Label": "Activity count", "Description": "Total number of events before pass to checkout", "type": "number"},
            {"Label": "Past # sessions", "Description": "Total number of past sesions of current user", "type": "number"},
         ]

# Categorical Fields with their Options
fields_categorical = [
                        {
                            "Label": "Condition",
                            "Options": ["Bom", "Bom - Sem Touch ID", "Excelente", "Muito Bom", "Novo"], # 5
                            "Description": "Quality Condition of the Device",
                            "type": "select"
                        },
                        {
                            "Label": "Storage",
                            "Options": ["128GB", "16GB", "1TB", "256GB", "32GB", "32GB RAM 2GB", "32GB RAM 3GB", "4GB", "512GB", "512MB", "64GB", "64GB RAM:4GB", "64GB RAM:6GB", "8GB"], #14
                            "Description": "Storage Capacity of the device",
                            "type": "select"
                        },
                        {
                            "Label": "Brand",
                            "Options": ["Asus", "Huawei", "LG", "Lenovo", "Motorola", "Multilaser", "Positivo", "Quantum", "Samsung", "Sony", "Xiaomi", "iPad", "iPhone"], # 13
                            "Description": "Brand of the device",
                            "type": "select"
                        }
                     ]