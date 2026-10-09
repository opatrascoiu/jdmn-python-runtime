#
# Copyright 2016 Goldman Sachs.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
from unittest import TestCase

from jdmn.runtime.annotation.AnnotationSet import AnnotationSet


class AnnotationSetTest(TestCase):

    def testAddWithoutName(self):
        annotationSet = AnnotationSet()
        annotationSet.addAnnotation("decision1", 0, "annotation1")
        annotationSet.addAnnotation("decision1", 1, "annotation2")
        annotationSet.addAnnotation("decision2", 0, "annotation3")

        self.assertEqual(3, len(annotationSet))
        self.assertEqual("decision1", annotationSet[0].decisionName)
        self.assertEqual(1, annotationSet[0].ruleIndex)
        self.assertEqual("annotation1", annotationSet[0].annotation)

    def testAddWithName(self):
        annotationSet = AnnotationSet()
        annotationSet.addAnnotation("decision1", 0, "name1", "annotation1")
        annotationSet.addAnnotation("decision1", 1, "name2", "annotation2")
        annotationSet.addAnnotation("decision2", 0, "name3", "annotation3")

        self.assertEqual(3, len(annotationSet))
        self.assertEqual("decision1", annotationSet[0].decisionName)
        self.assertEqual(1, annotationSet[0].ruleIndex)
        self.assertEqual("name1#annotation1", annotationSet[0].annotation)
