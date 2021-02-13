"""
A direct child CAN define required class variables (pseudo "abstract"),
but it is not necessary if the variables are defined by its child.
But in this case you have to define all the required class variables in an intermediate class.
"""


class ClassWithAbstractVariables(object):

    __required_class_variables = [
    ]

    @classmethod
    def check_required_class_variables(cls, child):
        parent = cls
        # print('\n----------\n', cls, '\n', parent, '\n', child)
        parent__required_class_variables = '_' + parent.__name__ + '__required_class_variables'
        child__required_class_variables = '_' + child.__name__ + '__required_class_variables'
        if hasattr(parent, parent__required_class_variables):
            for var in getattr(parent, parent__required_class_variables):
                # print('var ', var,
                #       '\nchild.__dict__ ', child.__dict__,
                #       '\nhasattr(child, var): ', hasattr(child, var))
                if not hasattr(child, var):
                    if ((not hasattr(child, child__required_class_variables)) or
                            (var not in getattr(child, child__required_class_variables))):
                        raise NotImplementedError(
                            f'Class {child} lacks required `{var}` class attribute'
                        )

    # You must define the method in a child intermediate class
    # @classmethod
    # def __init_subclass__(cls):
    #     super().__thisclass__.check_required_class_variables(child=cls)
    #     super().__init_subclass__()
