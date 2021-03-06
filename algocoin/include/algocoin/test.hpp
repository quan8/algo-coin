#include <iostream>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

#ifndef __ALGOCOIN_TEST_HPP__
#define __ALGOCOIN_TEST_HPP__
void say_hello(const char* name);


BOOST_PYTHON_MODULE(test)
{
    boost::python::def("say_hello", say_hello);
}
#endif