from typing import List, Tuple, Dict
import json
from functools import cache


@cache
def calculate_panels(
    panel_width: int, panel_height: int, roof_width: int, roof_height: int
) -> int:
    if roof_width <= 0 or roof_height <= 0:
        return 0

    if panel_width <= 0 or panel_height <= 0:
        return float("inf")

    (
        normal_panels,
        rotated_panels_rotated_roof,
        rotated_panels,
        normal_panels_rotated_roof,
    ) = 0, 0, 0, 0

    if roof_height >= panel_height and roof_width >= panel_width:
        normal_panels = calculate_panels(
            panel_width, panel_height, roof_width, roof_height - panel_height
        ) + (roof_width // panel_width)

        rotated_panels_rotated_roof = calculate_panels(
            panel_height, panel_width, roof_height, roof_width - panel_width
        ) + (roof_height // panel_height)

    if roof_height >= panel_width and roof_width >= panel_height:
        rotated_panels = calculate_panels(
            panel_width, panel_height, roof_width, roof_height - panel_width
        ) + (roof_width // panel_height)

        normal_panels_rotated_roof = calculate_panels(
            panel_width, panel_height, roof_height, roof_width - panel_height
        ) + (roof_height // panel_width)

    return max(
        normal_panels,
        rotated_panels,
        normal_panels_rotated_roof,
        rotated_panels_rotated_roof,
    )


def run_tests() -> None:
    with open("test_cases.json", "r") as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"],
            }
            for test in data["testCases"]
        ]

    print("Corriendo tests:")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
