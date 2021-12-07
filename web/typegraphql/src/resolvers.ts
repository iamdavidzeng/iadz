import { Arg, Authorized, Mutation, Query, Resolver } from 'type-graphql';
import { sampleRecipes } from './recipe.helpers';
import { Recipe } from './recipe.type';

@Resolver()
export class ExampleResolver {
  private recipesData: Recipe[] = sampleRecipes.slice();

  @Query((returns) => [Recipe])
  async recipes(): Promise<Recipe[]> {
    return await this.recipesData;
  }

  @Authorized()
  @Mutation()
  addRecipe(
    @Arg('title') title: string,
    @Arg('description', { nullable: true }) description?: string
  ): Recipe {
    const newRecipe = Object.assign(new Recipe(), {
      title,
      description,
      ratings: [],
    });
    this.recipesData.push(newRecipe);
    return newRecipe;
  }

  @Authorized('ADMIN')
  @Mutation()
  deleteRecipe(@Arg('title') title: string): boolean {
    const foundRecipeIndex = this.recipesData.findIndex(
      (it) => it.title === title
    );
    if (!foundRecipeIndex) {
      return false;
    }
    this.recipesData.splice(foundRecipeIndex, 1);
    return true;
  }
}
