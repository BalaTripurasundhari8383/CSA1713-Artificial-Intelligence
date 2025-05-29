# Define the CSP class
class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables          # List of regions
        self.domains = domains.copy()       # Dict: region -> list of possible colors
        self.neighbors = neighbors          # Dict: region -> list of neighboring regions
        self.assignment = {}                # Final color assignment

    def is_consistent(self, var, value):
        # Check if assigning value to var conflicts with neighbors
        for neighbor in self.neighbors[var]:
            if neighbor in self.assignment and self.assignment[neighbor] == value:
                return False
        return True

    def select_unassigned_variable(self):
        # Minimum Remaining Values (MRV) heuristic
        unassigned = [v for v in self.variables if v not in self.assignment]
        return min(unassigned, key=lambda var: len(self.domains[var]))

    def backtrack(self):
        # If all variables assigned, return assignment
        if len(self.assignment) == len(self.variables):
            return self.assignment

        var = self.select_unassigned_variable()
        for value in self.domains[var]:
            if self.is_consistent(var, value):
                self.assignment[var] = value

                # Forward checking: remove value from neighbors' domains
                removed = self.forward_check(var, value)

                result = self.backtrack()
                if result:
                    return result

                # Backtrack
                del self.assignment[var]
                self.restore_domains(removed)

        return None

    def forward_check(self, var, value):
        removed = []
        for neighbor in self.neighbors[var]:
            if neighbor not in self.assignment and value in self.domains[neighbor]:
                self.domains[neighbor].remove(value)
                removed.append((neighbor, value))
        return removed

    def restore_domains(self, removed):
        for var, value in removed:
            self.domains[var].append(value)

# Example: Map of Australia
if __name__ == "__main__":
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    colors = ['Red', 'Green', 'Blue']
    domains = {var: colors[:] for var in variables}
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    csp = MapColoringCSP(variables, domains, neighbors)
    solution = csp.backtrack()

    if solution:
        print("Solution:")
        for region in sorted(solution):
            print(f"{region}: {solution[region]}")
    else:
        print("No solution found.")
