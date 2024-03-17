import openai 
import re
from collections import Counter
import xmltodict
import AdversaGen as ag

if __name__ == '__main__':
    # load database
    with open('adversaGen.xml', 'r', encoding='utf-8') as file:
        database = file.read()

    # create AdversaGen object
    key = 'API_KEY_HERE!!!!'
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

    adversaGen = ag.AdversaGen(key, messages)

    dict_db = list(xmltodict.parse(database).values())[0]
    true_positive = 0
    
    for person_no in range(0, len(dict_db["row"])):
        name = dict_db["row"][person_no]["name"]
        label = dict_db["row"][person_no]["disease"].lower()
        label = re.sub('[^A-Za-z0-9]+', '', label)
        phenotypes = dict_db["row"][person_no]["phenotype"]
        if isinstance(phenotypes, str):
            phenotypes = [phenotypes]
        snps = []
        query1 = "List the rsID of some SNPs that have been identified as potentially contributing to the " \
                 "development of the disease linked to the following phenotypes: "
        for phenotype in phenotypes:
            query1 += phenotype + ", "
        query1 += " answer in single word bullet points."

        response1 = ""
        response2 = ""
        response3 = ""
        queries = []
        diseases = []
        try:
            while True:
                #response1 = bot.ask(query1).lower()
                response1 = adversaGen.make_call(query1)
                if response1 == "unusable response produced, maybe login session expired. try 'pkill firefox' and 'chatgpt install'":
                    print("unusable response produced, maybe login session expired. try 'pkill firefox' and 'chatgpt "
                          "install")
                    exit()
                snps = re.findall(r'rsi?d?_?\d+', response1)
                if len(snps) != 0:
                    # print(snps)
                    break

            query2 = "Pretend you are a researcher using chatGPT as a tool. Given a person with the following " \
                     "phenotypes: "
            for phenotype in phenotypes:
                query2 += phenotype + ", "
            query2 += " and the following SNPs: "
            for snp in snps:
                query2 += snp + ", "
            query2 += " What are 4 queries (in bullet points) that you would ask chatGPT to infer what genetic " \
                      "disease this person has? The queries should ask question such that the answers are a only list " \
                      "of genetic diseases."
            while True:
                response2 = adversaGen.make_call(query2) #response2 = bot.ask(query2).lower()
                if response2 == "unusable response produced, maybe login session expired. try 'pkill firefox' and 'chatgpt install'":
                    print("unusable response produced, maybe login session expired. try 'pkill firefox' and 'chatgpt "
                          "install")
                    exit()
                queries = response2.split("-")[1:5]
                if len(queries) != 0:
                    # print(queries)
                    break

            for query in queries:
                query += " Please answer in bullet points with one or more disease names only."
                while True:
                    response3 = adversaGen.make_call(query) #response3 = bot.ask(query).lower()
                    if response3 == "unusable response produced, maybe login session expired. try 'pkill firefox' and 'chatgpt install'":
                        print(
                            "unusable response produced, maybe login session expired. try 'pkill firefox' and 'chatgpt "
                            "install")
                        exit()
                    #print("Q: " + query)
                    #print("A: " + response3)
                    print("--------------------------------------")
                    diseases.append(response3.split('-')[1:])
                    if len(diseases) != 0:
                        print(diseases)
                        break

            diseases = [d for sublist in diseases for d in sublist]


            print(diseases)

            def get_letters(disease):
                return re.sub(r'[^a-zA-Z]', '', disease)


            diseases = [get_letters(d) for d in diseases]
            # print(diseases)

            # diseases_counts = Counter(diseases)
            diseases_counts = dict(sorted(dict(Counter(diseases)).items(), key=lambda x: x[1], reverse=True))
            prediction = list(diseases_counts.keys())[0]
            print(diseases_counts)
            if label in prediction:
                print("--------------------------------------")
                print("Correctly predicted label", label)
                print("--------------------------------------")
                true_positive += 1
            else:
                print("--------------------------------------")
                print("Incorrectly predicted label", label)
                print("--------------------------------------")
            #bot.refresh_session()
        except:
            pass
    accuracy = true_positive/len(dict_db["row"])
    print("Accuracy = ", accuracy)
    print("--------------------------------------")
    print("--------------------------------------")
    print()
    print()


