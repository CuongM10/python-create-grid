import math


def generate_arrowhead_grid_800_nodes():
    """
    Tạo lưới arrowhead với 800 nodes (20 dãy x 40 nodes/dãy)
    Theo quy luật từ hình mẫu:
    - Dãy 1 (y=0): (0,0), (5,3), (10,0), (15,3), (20,0), (25,3)...
    - Dãy 2 (y=10): (0,10), (5,13), (10,10), (15,13), (20,10), (25,13)...
    """

    nodes = []

    # Thông số từ hình mẫu
    base_spacing_x = 5  # Khoảng cách cơ bản theo x
    base_spacing_y = 10  # Khoảng cách giữa các dãy
    zigzag_height = 3  # Độ cao zigzag (lên xuống)

    # Tạo 20 dãy, mỗi dãy 40 nodes
    for row in range(20):  # 20 dãy (từ 0 đến 19)
        y_base = row * base_spacing_y  # y = 0, 10, 20, 30, ...

        for col in range(40):  # 40 nodes mỗi dãy (từ 0 đến 39)
            x = col * base_spacing_x
            y = y_base if col % 2 == 0 else y_base + zigzag_height
            nodes.append([x, y])

    return nodes


def save_nodes_to_file(nodes, filename="arrowhead_nodes_800.py"):
    """
    Lưu danh sách 800 nodes vào file Python (không thêm comment đánh số node)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Tọa độ 800 nodes của lưới arrowhead\n")
        f.write("# 20 dãy x 40 nodes/dãy\n")
        f.write("# Sắp xếp từ trái qua phải, từ dưới lên trên\n\n")
        f.write("nodes = [\n")

        for node in nodes:
            f.write(f"    [{node[0]}, {node[1]}],\n")

        f.write("]\n\n")
        f.write(f"# Tổng số nodes: {len(nodes)}\n")
        f.write("# Cấu trúc: 20 dãy x 40 nodes/dãy = 800 nodes\n")


# Ví dụ sử dụng
if __name__ == "__main__":
    nodes = generate_arrowhead_grid_800_nodes()
    save_nodes_to_file(nodes)
    print(f"Đã lưu {len(nodes)} nodes vào file 'arrowhead_nodes_800.py'")
