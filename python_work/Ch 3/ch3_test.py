#Try it yourself review for Chapter 3
world_sites = []
world_sites.append('Thailand')
world_sites.append('Hawaii')
world_sites.append('Venice')
print(world_sites)
world_sites.insert(0,'Puerto Rico')
world_sites.insert(1,'Japan')
print(sorted(world_sites))
print(sorted(world_sites, reverse=True))
print(world_sites)
world_sites.reverse()
print(world_sites)
world_sites.reverse()
print(world_sites)
world_sites.sort()
print(world_sites)
world_sites.sort(reverse = True)
print(f'\n\t This is the first place I would like to visit in our first world tour \n\t {world_sites[4].title()}!')