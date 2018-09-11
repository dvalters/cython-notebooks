#include <vector>

#ifndef stdvector_H
#define stdvector_H

std::vector<float> get_a_vec()
{
    std::vector<float> gh;
    for (int i = 0; i<500; i++){
        gh.push_back(i);
    }
    return gh;
}
