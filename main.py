import xml.etree.ElementTree as ET

full_xml_file = "export_full.xml"
part_xml_file = "part_export.xml"


def countProducts(xml_file):
    """
    Count amounts of products
    :param xml: xml file with products
    :return: print to console amount of products
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for elem in root.iter():
        if elem.tag == "items":
            count = 0
            for child in elem:
                if child.tag == "item":
                    count += 1
            print("Produktů: ", count)


def printProducts(xml_file):
    """
    Print list of all products
    :param xml: xml file with products
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag == "items":
            for child in elem:
                if child.tag != "item":
                    continue
                print("---", child.attrib["name"], "---")


def printProductsWithSpareParts(xml_file):
    """
    Print list of all products and there spare parts, if there are some
    :param xml: xml file with products
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag == "items":
            for child in elem:
                if child.tag != "item":
                    continue
                print("---", child.attrib["name"], "---")

                for item in child:
                    if item.tag == "parts":
                        for part in item:
                            if part.attrib["categoryId"] == '1':
                                print(part.attrib["name"], ":")
                                for it in part.iter():
                                    if it.tag == "item":
                                        print("    ", it.attrib["name"])


def doAllTasks(xml_file):
    """
    count all product and print their name + prints name of their spare parts
    :param xml:
    :return:
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag == "items":
            count = 0
            for child in elem:
                if child.tag == "item":
                    count += 1
            print("Produktů: ", count)
            for child in elem:
                if child.tag != "item":
                    continue
                print("---", child.attrib["name"], "---")

                for item in child:
                    if item.tag == "parts":
                        for part in item:
                            if part.attrib["categoryId"] == '1':
                                print(part.attrib["name"], ":")
                                for it in part.iter():
                                    if it.tag == "item":
                                        print("    ", it.attrib["name"])


if __name__ == '__main__':
    xml_file = full_xml_file

    use_part_file = False
    while True:
        print("Zvolte si prosím jednu z možností:")
        print("1 - vypsat počet produktů")
        print("2 - vypsat seznam produktů")
        print("3 - vypsat seznam produktů spolu s náhradními díly")
        print("4 - vypsat celkový počet produktů a  seznam produktů s náhradními díly")

        if use_part_file:
            print("\nc - změnit XML soubor z part_export.xml na export_full.xml")
        else:
            print("\nc - změnit XML soubor z export_full.xml na part_export.xml")

        print("\ne - ukončit program")
        input1 = input()

        if input1 == "1":
            countProducts(xml_file)
        elif input1 == "2":
            printProducts(xml_file)
        elif input1 == "3":
            printProductsWithSpareParts(xml_file)
        elif input1 == "4":
            doAllTasks(xml_file)
        elif input1 == "c":
            if use_part_file:
                xml_file = full_xml_file
                use_part_file = False
            else:
                xml_file = part_xml_file
                use_part_file = True
        elif input1 == "e":
            break
