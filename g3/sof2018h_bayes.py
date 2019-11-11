from bayes_net import BayesNet

def main():
    print("Probabilidade Conjunta:", bn.jointProb([('ST', True), ('UPAL', True), ('CEA', False), ('CP', True), ('PA', True), ('FEUR', False)]))
    print("Probabilidade Individual:", bn.indProb(("CEA", False)))

if __name__ == '__main__':
    bn = BayesNet()

    bn.add("ST", [], 0.60)
    bn.add("UPAL", [], 0.05)

    bn.add("CP", [("ST", True), ("PA", False)], 0.01)
    bn.add("CP", [("ST", True), ("PA", True)], 0.02)
    bn.add("CP", [("ST", False), ("PA", False)], 0.001)
    bn.add("CP", [("ST", False), ("PA", True)], 0.011)

    bn.add("CEA", [("ST", True)], 0.90)
    bn.add("CEA", [("ST", False)], 0.001)


    bn.add("PA", [("UPAL", True)], 0.25)
    bn.add("PA", [("UPAL", False)], 0.04)
    
    bn.add("FEUR", [("UPAL", False), ("PA", True)], 0.10)
    bn.add("FEUR", [("UPAL", False), ("PA", False)], 0.01)
    bn.add("FEUR", [("UPAL", True), ("PA", True)], 0.90)
    bn.add("FEUR", [("UPAL", True), ("PA", False)], 0.90)

    main()