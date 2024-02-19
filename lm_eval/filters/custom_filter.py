from lm_eval.api.filter import Filter
import json


class TopKAccFilter(Filter):

    """
    A filter which evaluates
    """

    # name = "track_decontamination"

    def __init__(self) -> None:
        """
        write doc.
        """

    def apply(self, resps, docs):

        # print(f"resps in custom filter = {resps}")
        # print(f"type(resps) = {type(resps)}")

        print(f"docs in custom filter = {docs}")
        print(f"type(docs) = {type(docs)}")

        def dict_to_list(topk_dict, k=5):

            ordered_list = []

            # Loop through keys from top_1 to top_k
            for i in range(1, k+1):
                key = "top_" + str(i)
                if key in topk_dict:
                    ordered_list.append(topk_dict[key])
                        
            return ordered_list


        def apply_to_resp(resp): # resp is a list of json strings.

            topk_dicts = [json.loads(json_str) for json_str in resp] 

            return [dict_to_list(topk_dict) for topk_dict in topk_dicts]



        filtered_resps = [apply_to_resp(resp) for resp in resps]

        print(f"filtered_resps in custom filter = {filtered_resps}")
        print(f"type(filtered_resps) = {type(filtered_resps)}") 

        return filtered_resps
