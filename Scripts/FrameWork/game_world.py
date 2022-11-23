# layer 0: Background Objects
# layer 1: Foreground Objects

class GameWorld:
    def __init__(self):
        self.objects = [[], []]
        self.collision_group = dict()

    def add_object(self, o, depth):
        if len(self.objects) <= depth:
            for i in range(depth - len(self.objects) + 1):
                self.objects.append([])

        self.objects[depth].append(o)

    def add_objects(self, ol, depth):
        """

        :rtype: object
        """
        if len(self.objects) <= depth:
            for i in range(depth - len(self.objects) + 1):
                self.objects.append([])

        self.objects[depth] += ol

    def remove_object(self, o):
        for layer in self.objects:
            if o in layer:
                layer.remove(o)
                # 충돌 그룹(리스트)에서도 객체를 삭제
                self.remove_collision_object(o)
                del o
                return
        #     try:
        #
        #     except:
        #         pass
        # raise ValueError('Trying destroy non existing object')

    def all_objects(self):
        for layer in self.objects:
            for o in layer:
                yield o

    def clear(self):
        for o in self.all_objects():
            del o
        for layer in self.objects:
            layer.clear()

    def add_collision_group(self, a, b, group):
        if group not in self.collision_group:
            self.collision_group[group] = [[], []]

        if a:
            if type(a) is list:
                self.collision_group[group][0] += a
            else:
                self.collision_group[group][0].append(a)

        if b:
            if type(b) is list:
                self.collision_group[group][1] += b
            else:
                self.collision_group[group][1].append(b)
        pass

    def all_collision_pairs(self):
        # collisiion_group라는 딕셔너리에서 각 리스트로부터 페어를 만들어서 보내준다.
        for group, pairs in self.collision_group.items():  # items() key, value
            for a in pairs[0]:
                for b in pairs[1]:
                    yield a, b, group

    def remove_collision_object(self, o):
        for pairs in self.collision_group.values():  # key:value에 해당되는 것만 가져온다
            if o in pairs[0]:
                pairs[0].remove(o)
            elif o in pairs[1]:
                pairs[1].remove(o)

    pass




