import { Field, Float, Int, ObjectType } from 'type-graphql';

@ObjectType()
export class Recipe {
  @Field()
  title: string;

  @Field({ nullable: true })
  description?: string;

  @Field((type) => [String])
  ingredients: string[];

  @Field((type) => [Int])
  ratings: number[];

  @Field((type) => Float, { nullable: true })
  get averageRating(): number | null {
    return this.ratings.reduce((a, b) => a + b, 0) / this.ratings.length;
  }
}
