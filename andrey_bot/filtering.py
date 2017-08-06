
class Filter(object):
    """
    Filters output
    """

    def acceptance_test(self, r):
        """
        Function that takes in response text and determines if it is acceptable.
        :param r: reponse text, basestring
        :return: bool indicating whether to the response is passed by the filter
        """
        raise NotImplementedError("You must use a non abstract Filter.")

class PreFilter(Filter):
    """
    Filters that happen before word replacement.
    """
    pass

class PostFilter(Filter):
    """
    Filters that happen after word replacement.
    """
    pass

class WordFilter(PreFilter):
    def __init__(self, word_list):
        """
        Creates a word filter. At least one of the words must appear in the output text in order for the output to
        be passed by the filter. Comparison is case insensitive.

        :param word_filter: list of basestrings (words)
        """
        self.word_list = word_list


    def acceptance_test(self, r):
        """
        Function that takes in response text and determines if it is acceptable.

        :param r: reponse text, basestring
        :return: bool indicating whether to the response is passed by the filter
        """
        if r is None:
            return False
        do_send = False
        rlower = r.lower()
        for word in self.word_list:
            # TODO fix scunthorpe problem
            if word.lower() in rlower:
                do_send = True
                break
        return do_send